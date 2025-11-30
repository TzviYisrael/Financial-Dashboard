// src/services/jwtService.ts
import { jwtDecode } from 'jwt-decode';

export interface JWTPayload {
  user_id: number;
  email: string;
  exp: number;
}

export const jwtService = {
  // Décoder le token
  decode: (token: string): JWTPayload | null => {
    try {
      return jwtDecode<JWTPayload>(token);
    } catch (error) {
      console.error('Error decoding token:', error);
      return null;
    }
  },

  // Vérifier si le token est expiré
  isTokenExpired: (token: string): boolean => {
    const decoded = jwtService.decode(token);
    if (!decoded) return true;

    const currentTime = Date.now() / 1000;
    return decoded.exp < currentTime;
  },

  // Récupérer le token du localStorage
  getToken: (): string | null => {
    return localStorage.getItem('token');
  },

  // Sauvegarder le token dans localStorage
  saveToken: (token: string): void => {
    localStorage.setItem('token', token);
  },

  // Supprimer le token
  removeToken: (): void => {
    localStorage.removeItem('token');
  }
};
