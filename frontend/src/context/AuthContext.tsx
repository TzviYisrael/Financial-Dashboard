// src/context/AuthContext.tsx
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { jwtService } from '../services/jwtService';

export interface User {
  id: number;
  email: string;
  name: string;
}


interface AuthContextType {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);

  // Au chargement, vérifier si un token existe
  useEffect(() => {
    const storedToken = jwtService.getToken();
    const storedUser = localStorage.getItem('user');

    if (storedToken && storedUser) {
      // Vérifier si le token n'est pas expiré
      if (!jwtService.isTokenExpired(storedToken)) {
        setToken(storedToken);
        setUser(JSON.parse(storedUser));
      } else {
        // Token expiré, on nettoie
        jwtService.removeToken();
        localStorage.removeItem('user');
      }
    }
  }, []);

  const login = (user: User, token: string) => {
    setUser(user);
    setToken(token);
    jwtService.saveToken(token);
    localStorage.setItem('user', JSON.stringify(user));
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    jwtService.removeToken();
    localStorage.removeItem('user');
  };

  const isAuthenticated = !!user && !!token;

  return (
    <AuthContext.Provider value={{ user, token, login, logout, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
