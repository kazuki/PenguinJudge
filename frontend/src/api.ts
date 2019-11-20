export interface User {
  id: string;
  name: string;
  admin: boolean;
  created: string;
}

export interface Environment {
  id: number;
  name: string;
}

export interface Problem {
  id: string;
  title: string;
  description: string;
  time_limit: number;
  memory_limit: number;
  score: number;
}

export interface Contest {
  id: string;
  title: string;
  description: string;
  start_time: string;
  end_time: string;
  problems: Array<Problem> | null;
}

export interface PartialSubmission {
  contest_id: string;
  problem_id: string;
  code: string;
  environment_id: number;
}

export interface Submission extends PartialSubmission {
  id: number;
  status: string;
  created: string;
  user_id: string;
}

export interface Token {
  token: string;
  expires_in: number;
}

export interface ListContestsFilter {
  status?: string;
}

export class API {
  private static _fetch<T>(url: string, init?: RequestInit): Promise<T> {
    // 以下の情報を返却するPromiseを返す
    // [成功した場合]
    //   <jsonパース成功> resolve(T)
    //   <jsonパース失敗> reject(undefined)
    // [サーバからエラーが返却された場合]
    //   reject({status: HTTPステータスコード, json: bodyが含まれる場合})
    // [サーバとの通信が切断された場合]
    //   reject(undefined)
    return new Promise((resolve, reject) => {
      fetch(url, init).then(resp => {
        if (resp.ok) {
          resp.json().then(resolve).catch(_ => reject(undefined));
        } else {
          resp.json().then(body => {
            reject({ status: resp.status, json: body });
          }, _ => {
            reject({ status: resp.status, json: undefined });
          });
        }
      }, _ => {
        reject(undefined);
      });
    });
  }

  static get_current_user(): Promise<User> {
    return API._fetch('/api/user');
  }

  static list_contests(filter?: ListContestsFilter): Promise<Array<Contest>> {
    let q = '';
    if (filter) {
      let tmp = [];
      if (filter.status)
        tmp.push('status=' + encodeURIComponent(filter.status))
      if (tmp)
        q = '?' + tmp.join('&');
    }
    return API._fetch('/api/contests' + q);
  }

  static get_contest(id: string): Promise<Contest> {
    return API._fetch('/api/contests/' + encodeURIComponent(id));
  }

  static list_environments(): Promise<Array<Environment>> {
    return API._fetch('/api/environments');
  }

  static submit(submission: PartialSubmission): Promise<Submission> {
    const contest_id = submission.contest_id;
    delete submission.contest_id;
    const path = '/api/contests/' + encodeURIComponent(contest_id) + '/submissions';
    return API._fetch(path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(submission)
    });
  }

  static list_submissions(contest_id: string): Promise<Array<Submission>> {
    return API._fetch(
      '/api/contests/' + encodeURIComponent(contest_id) + '/submissions');
  }

  static login(id: string, password: string): Promise<Token> {
    return API._fetch('/api/auth', {
      method: 'POST',
      credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        id,
        password,
      })
    });
  }
}
