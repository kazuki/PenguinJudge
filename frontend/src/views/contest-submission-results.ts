import { customElement, LitElement, html, css } from 'lit-element';
import { Subscription } from 'rxjs';
import { API, Submission } from '../api';
import { router, session } from '../state';
import { format_datetime_detail } from '../utils';

@customElement('penguin-judge-contest-submission-results')
export class PenguinJudgeContestSubmissionResults extends LitElement {
  contestEnvSubscription: Subscription | null = null;
  subscription: Subscription | null = null;
  submissions: Submission[] = [];
  languageNames: { [key: number]: string } = {};

  constructor() {
    super();
    this.contestEnvSubscription = session.environment_subject.subscribe((s) => {
      this.languageNames = s.reduce((obj: { [key: number]: string }, { id, name }) => {
        obj[id] = name;
        return obj;
      }, {});
    });
    this.subscription = session.contest_subject.subscribe((s) => {
      if (s) {
        API.list_submissions(s.id).then((submissions) => {
          this.submissions = submissions;
          this.requestUpdate();
        });
      }
    });
  }

  disconnectedCallback() {
    super.disconnectedCallback();
    if (this.contestEnvSubscription) {
      this.contestEnvSubscription.unsubscribe();
      this.contestEnvSubscription = null;
    }
    if (this.subscription) {
      this.subscription.unsubscribe();
      this.subscription = null;
    }
  }

  render() {
    if (!session.contest) {
      return html``;
    }

    const nodes = this.submissions.map(s => {
      const url = router.generate('contest-submission', { id: session.contest!.id, submission_id: s.id });
      return html`<tr><td>${format_datetime_detail(s.created)}</td><td>${[s.problem_id]}</td><td>${s.user_id}</td><td>${this.languageNames[s.environment_id]}</td><td>${s.status}</td><td><a is="router_link" href="${url}">詳細</td></tr>`;
    });
    return html`
      <table>
        <thead><tr><td>提出日時</td><td>問題</td><td>ユーザ</td><td>言語</td><td>結果</td><td></td></tr></thead>
        <tbody>${nodes}</tbody>
      </table>`;
  }

  static get styles() {
    return css`
    table {
      border-collapse:collapse;
    }
    td {
      border: 1px solid #bbb;
      padding: 0.5ex 1ex;
    }
    thead td {
      font-weight: bold;
      text-align: center;
    }
    `;
  }
}
