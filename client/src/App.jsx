import { useState, useEffect } from 'react'
import viteLogo from '/vite.svg'
import {FaSearch} from "react-icons/fa";
import axios from 'axios'
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { ThemeProvider } from './theme/ThemeContext';
import ToggleThemeButton from './components/ToggleThemeButton';
import './App.css'

function App() {
  const [options, setOptions] = useState('Category')
  const [query, setQuery] = useState('')
  const [results,setResults] = useState([])
  const postData = {
    key1: query,
    key2: options.toLowerCase()
  }
  //localhost server link to server.py
  const apiUrl = 'http://127.0.0.1:5000'
  useEffect(() => {
    const delayTimer = setTimeout(() => {
      // Make a request to your search endpoint when the user stops typing
      if (query.trim() !== '') {

     axios.post(apiUrl,postData).then((response) => setResults(response.data)).catch((error) => console.error(error) )
          
      }
    }, 500); // Adjust the delay (in milliseconds) as needed

    // Cleanup the timer on component unmount or when the query changes
    return () => clearTimeout(delayTimer);
  }, [query]);
  
const handleChange = (e) => {
  
    setQuery(e.target.value)
  }
  return (
      <ThemeProvider>
      <Router>
    <div className='App'>
    <div className='blank'></div>
      <div className='options'>
        <div className={options === 'Category' ? 'selected' : 'notSelected'} onClick={() => setOptions('Category')}>Category</div>
        <div className={options === 'Brand' ? 'selected' : 'notSelected'} onClick={() => setOptions('Brand')}>Brand</div>
        <div className={options === 'Retailer' ? 'selected' : 'notSelected'} onClick={() => setOptions('Retailer')}>Retailer</div>
        <ToggleThemeButton/>
      </div>
      <div className='input-wrapper'>
        <FaSearch className='FaSearch' size={20} color='#535353' />
      <input placeholder='Type to search...'
      value={query}
      onChange={handleChange} />
      </div>
      <div
       className='results'>
        <table>
    <thead>
        <tr>
          <th>
            Offer
          </th>
          <th>
            Similarity Score
          </th>
        </tr>
    </thead>
  <tbody>
    {
  results.length > 0 ?
results.map((result, index) => (
  <tr>
    <td>{result.OFFER}
  </td>
  <td>
  {result.SIMILARITY_SCORE}</td>

  </tr>

)):
<tr>
  <td>No offers found</td>
  <td>-</td>
  </tr>
    }
    </tbody>
        </table>
       </div>
    </div>
       </Router>
    </ThemeProvider>
  )
}

export default App
