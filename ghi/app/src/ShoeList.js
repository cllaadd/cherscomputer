import { NavLink } from "react-router-dom";
import {useEffect, useState} from 'react';


// async function ShoesList() {
//   const response = await fetch('http://localhost:8080/api/shoes');
//   if (response.ok) {
//     const data = await response.json();
//     console.log(data);
//   } else {
//     console.error(response);
//   }
function ShoesList(props) {
  const [shoes, setShoes] = useState([])

  const getData = async() => {
      const response = await fetch('http://localhost:8080/api/shoes/')
      const data = await response.json()

      setShoes(data)
  }

  const handleDelete = async(id) => {
      const response = await fetch(`http://localhost:8080/api/shoes/${id}/`, {method:"DELETE"})
      const data = await response.json()
      getData();
      window.location = "/shoes"
  }

    return (
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Manufacturer</th>
                <th>Color</th>
                <th>Model</th>
              </tr>
            </thead>
            <tbody>
            {/* {shoes?.map(shoe => {
              console.log(shoe)
              return (
                <tr key={shoe.href}>
                  <td>{ shoe.manufacturer }</td>
                  <td>{ shoe.color }</td>
                  <td>{ shoe.model_name }</td>
                </tr>
              );
            })} */}
            </tbody>
          </table>
      );
}



export default ShoesList;
