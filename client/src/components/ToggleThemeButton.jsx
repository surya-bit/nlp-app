import React from 'react';
import { useTheme } from '../theme/ThemeContext';

const ToggleThemeButton = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme} className="toggle-theme-button">
      Toggle {theme === 'light' ? 'Dark' : 'Light'} Mode
    </button>
  );
};

export default ToggleThemeButton;
