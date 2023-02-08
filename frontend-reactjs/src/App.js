import { BrowserRouter as Router, Routes as Switch, Link, Route} from 'react-router-dom';

import './App.css';

//import LoginPage from './pages/login-class';
import LoginPage from './pages/login-function';
import NotFoundPage from './pages/not-found';


function App() {
  return (
    <>
      <Router>
        <Switch>
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
