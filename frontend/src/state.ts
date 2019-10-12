import Navigo from 'navigo';
import { BehaviorSubject } from 'rxjs';

import { API, Contest, Environment } from './api';

export const router: any = new Navigo(null, true, '#!');

class Session {
  // Authentication
  token: string | null = null;
  get logged_in(): boolean {
    return this.token !== null;
  }

  // Environment
  private _envs = new BehaviorSubject<Array<Environment>>([]);
  get environment_subject() { return this._envs; }
  get environments() { return this._envs.value; }

  // Contest
  private _contest = new BehaviorSubject<Contest | null>(null);
  enter_contest(id: string): Promise<Contest> {
    if (!id)
      throw 'BUG: context_id must not be null';
    return new Promise((resolve, reject) => {
      if (this.contest && this.contest.id === id) {
        resolve(this.contest);
        return;
      }
      API.get_contest(id).then((c) => {
        resolve(c);
        this._contest.next(c);
      }).catch(reject);
    });
  }
  leave_contest() {
    if (this.contest)
      this._contest.next(null);
  }
  get contest() {
    return this._contest.value;
  }
  get contest_subject() { return this._contest; }
  task_id: string | null = null;

  // Init
  init() {
    API.list_environments().then((envs) => {
      if (envs)
        this._envs.next(envs);
    });
  }
}
export const session = new Session();
