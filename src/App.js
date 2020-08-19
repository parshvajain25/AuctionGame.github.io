import React from 'react';
import './App.css';
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';

import Admin from './components/admin';
import Home from './components/home';
import Player from './components/players';
import Rules from './components/rules';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      speed: 10,
    };
  }

  componentDidMount() {
    this.setState({
      speed: 30,
    });
  }

  render() {
    return (
      <Router>
        <div id="nav-bar">
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/players">Players</Link>
            </li>
            <li>
              <Link to="/rules">Rules</Link>
            </li>
          </ul>
        </div>

        <div id="main-content">
          <Switch>
            <Route path="/players">
              <Player />
            </Route>
            <Route path="/rules">
              <Rules />
            </Route>
            <Route path="/">
              <Home />
            </Route>
            <Route path="/admin">
              <Admin />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
