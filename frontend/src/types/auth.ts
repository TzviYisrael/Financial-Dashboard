export interface User {
  id: number;
  email: string;
  name: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface LoginResponse {
  id: number;
  email: string;
  name: string;
  message: string;
}