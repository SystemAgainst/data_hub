import api from './http'

export const login = (credentials: { username: string; password: string }) =>
  api.post<{ token: string }>('auth/', credentials)
