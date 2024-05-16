import React from "react";
// import zxcvbn from "zxcvbn";

const PasswordStrengthMeter = ({ password }) => {
  let score = 0;

  // Length
  if (password.length >= 20) {
    score++;
  }

  // Uppercase letters
  if (/[A-Z]/.test(password)) {
    score++;
  }

  // Lowercase letters
  if (/[a-z]/.test(password)) {
    score++;
  }

  // Numbers
  if (/[0-9]/.test(password)) {
    score++;
  }

  // Special Symbols
  if (/[^A-Za-z0-9]/.test(password)) {
    score++;
  }

  const overallScore = score;

  const progressPercentage = (overallScore * 100) / 5;

  const strengthLevels = [
    "Very Weak, how can there be a password with no password:).",
    "Weak, Cracked in minutes.",
    "Fair, will take some time to get cracked.",
    "Good, Beyond Fair, will take some hours to get cracked.",
    "Strong, will take months to be cracked.",
    "Very Strong, will take several years to be cracked.",
  ];
  const strength = strengthLevels[overallScore];

  const funcProgressColor = () => {
    switch (overallScore) {
      case 0:
        return "#828282";
      case 1:
        return "#EA1111";
      case 2:
        return "#FFAD00";
      case 3:
        return "#9bc158";
      case 4:
        return "#00b500";
      case 5:
        return "#469c18";
      default:
        return "none";
    }
  };

  const changePasswordColor = () => ({
    width: `${progressPercentage}%`,
    background: funcProgressColor(),
    height: "7px",
  });

  return (
    <>
      <div className="progress" style={{ height: "7px" }}>
        <div className="progress-bar" style={changePasswordColor()}></div>
      </div>
      <p style={{ color: funcProgressColor() }}>{strength}</p>
    </>
  );
};

export default PasswordStrengthMeter;
