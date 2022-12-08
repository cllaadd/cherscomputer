import { NavLink } from "react-router-dom";
import {useEffect, useState} from 'react';


function ShoesList() {
  const [shoes, setShoes] = useState([])

  const getData = async() => {
      const response = await fetch('http://localhost:8080/api/shoes/')
      const data = await response.json()
      console.log(data)

      setShoes(data.shoes)
  }

  const handleDelete = async(id) => {
      const response = await fetch(`http://localhost:8080/api/shoes/${id}/`, {method:"DELETE"})
      const data = await response.json()
      getData();
      window.location = "/shoes"
  }

  useEffect(()=> {
    getData();
  }, [])

    return (
      <div>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Manufacturer</th>
                <th>Color</th>
                <th>Model</th>
                <th>Picture</th>
                <th>Bin</th>
              </tr>
            </thead>
            <tbody>
            {shoes?.map(shoe => {
              console.log(shoe)
              return (
                <tr key={shoe.id}>
                  <td>{ shoe.manufacturer }</td>
                  <td>{ shoe.color }</td>
                  <td>{ shoe.model_name }</td>
                  <td><img src={shoe.picture_url} className=" pic img-fluid"/></td>
                  <td>{shoe.bin.closet_name}</td>
                  <td>
                      <button className="btn btn-danger m-2" onClick={()=> {handleDelete(shoe.id)}}>Delete</button>
                 </td>
                </tr>
              );
            })}
            </tbody>
          </table>
          <NavLink className="btn btn-primary" id="new-shoe-link" aria-current="page" to ="new-shoe"> New Shoe</NavLink>
        </div>
      );
}



export default ShoesList;
