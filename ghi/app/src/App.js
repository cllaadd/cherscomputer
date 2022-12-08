import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './HatsList';
import HatForm from './HatForm';
import ShoesList from './ShoesList';
import ShoeForm from './ShoeForm';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
        
          <Route path="hats">
            <Route path="" element={<HatsList />} />
            <Route path="new" element= {<HatForm />} />
          </Route>

          <Route path="shoes">
            <Route path="" element={<ShoesList/>} />
            <Route path="new" element= {<ShoeForm />} />
          </Route>

        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
