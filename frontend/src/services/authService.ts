// src/services/authService.ts
import axios from 'axios';
import { LoginCredentials, LoginResponse } from '../types/auth';

const API_URL = 'http://localhost:8001/api/auth';

export const authService = {
  login: async (credentials: LoginCredentials): Promise<LoginResponse> => {
    const response = await axios.post(`${API_URL}/login`, credentials);
    return response.data;
  }
};
