import { useState } from "react";
import StrengthChecker from "./components/StrengthCheck";


function App() {
  const [password, setPassword] = useState("");
  return (
    <div className="container">
      <div className="col-md-6 mx-auto">
        <h3 className="text-center my-5">Password Complexity Checker</h3>
        <div className="form-group mb-1">
          <input
            type="text"
            className="form-control shadow-none"
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <StrengthChecker password={password} />
      </div>
    </div>
  );
}

export default App;
