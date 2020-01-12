import React from 'react';
import { BrowserRouter as Router, Switch,Route } from 'react-router-dom';
import Page from './Pages/Page';
import PageNotFound from './Pages/PageNotFound';
function App() {
  return (
    <Router>
        <Switch>
            <Route path='/' exact component={Page} />
            <Route path='**' exact component={PageNotFound} />
        </Switch>
    </Router>
  );
}

export default App;
