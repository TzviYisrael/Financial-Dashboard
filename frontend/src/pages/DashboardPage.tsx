// src/pages/DashboardPage.tsx
import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export const DashboardPage: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <h1 className="text-xl font-bold text-gray-800">
              Portfolio Copilot
            </h1>
            <button
              onClick={handleLogout}
              className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition duration-200"
            >
              Logout
            </button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-4 text-gray-800">
              Welcome, {user?.name}!
            </h2>
            <p className="text-gray-600 mb-6">
              Email: {user?.email}
            </p>
            <div className="bg-blue-50 border-l-4 border-blue-500 p-4">
              <p className="text-blue-700">
                🎉 You are successfully logged in to the Dashboard!
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};
