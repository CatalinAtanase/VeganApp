let accessToken: string;
let expiresAt: Date

// Use expires at to check if the token is expired before request and refresht the access token
// check quasar in chrome is done there

export const addMinutes = (minutes: number) => {
  let d = new Date()
  return new Date(d.getTime() + minutes * 60000)
}

export const setAccessToken = (s: string) => {
  accessToken = s;
};

export const getAccessToken = () => {
  return accessToken;
};

export const setExpiresAt = (d: Date) => {
  expiresAt = d;
};

export const getExpiresAt = () => {
  return expiresAt;
};

