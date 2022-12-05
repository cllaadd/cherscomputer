import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './HatsList';
import HatForm from './HatForm';
import ShoesList from './ShoeList';

function App(props) {
  if (props.hats === undefined) {
    return null;
  }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="hats">
            <Route path="" element={<HatsList hats={props.hats} />} />
            <Route path="new-hat" element= {<HatForm />} />
            {/* <Route path="delete-hat" element= {<DeleteHat />} /> */}
            </Route>
          <Route path="shoes">
            <Route path="" element={<ShoesList />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
