import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to React</h1> <img src= {logo} alt="logo" width="100" />
      <h3>
        30DaysOfCode | Getting Started with React | Day 9
        </h3>
        <a
          className="App-link"
          href="mrkrishna.me/30-days-of-code"
          target="_blank"
          rel="noopener noreferrer"
        >
          Repository Link
        </a>
        <br></br>
        <h3>Made with ❤ by Krishna Agarwal</h3>
      </header>
      <br></br>
      <img src= "cat.jpg" width="300" alt="end" />
      <h2>Bye 👋🏻</h2>
    </div>
  );
}

export default App;
