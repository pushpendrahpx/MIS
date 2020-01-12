import React from 'react';
import { BrowserRouter as Router, Switch,Route } from 'react-router-dom';
import Page from './Pages/Page';
import PageNotFound from './Pages/PageNotFound';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
        <Switch>
            <Route path='/' component={Page} />
            <Route path='**' component={PageNotFound} />
        </Switch>
    </Router>
  );
}

export default App;
