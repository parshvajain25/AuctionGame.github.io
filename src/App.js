import React from 'react';
import './App.css';
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';

import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

import Admin from './components/admin';
import Home from './components/home';
import Player from './components/players';
import Rules from './components/rules';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      speed: 10,
      tabValue: 0,
    };

    // Don't forget to bind the functions to classes
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.setState({
      speed: 30,
    });
  }

  handleChange(event, newValue) {
    this.setState({
      tabValue: newValue,
    });
    console.log('Handle Change', newValue);
  }

  render() {
    return (
      <Router>
        <AppBar position="static" color="transparent" id="nav-bar">
          <Tabs
            variant="fullWidth"
            aria-label="Navigation"
            value={this.state.tabValue}
            onChange={this.handleChange}
          >
            <Tab label="Home" to="/" component={Link} />
            <Tab label="Players" to="/players" component={Link} />
            <Tab label="Rules" to="/rules" component={Link} />
          </Tabs>
        </AppBar>

        <div id="main-content">
          <Switch>
            <Route path="/players">
              <Player />
            </Route>
            <Route path="/rules">
              <Rules />
            </Route>
            <Route path="/admin">
              <Admin />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
