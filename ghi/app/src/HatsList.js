import { NavLink } from "react-router-dom";

function HatsList(props) {
    const [hats, setHats] = useState([])

    const getData = async() => {
        const response = await fetch('http://localhost:8090/api/hats/')
        const data = await response.json()

        setJokes(data)
    }

    const handleDelete = async(id) => {
        const response = await fetch(`http://localhost:8090/api/hats/${id}/`, {method:"DELETE"})
        const data = await response.json()
        getData();
        window.location = "/new"
    }
    return (
        <div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Color</th>
                        <th>Fabric</th>
                        <th>Style</th>
                        <th>Picture</th>
                        <th>Location</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {props.hats?.map(hat => {
                        console.log(hat)
                        return (
                            <tr key={hat.id}>
                                <td>{hat.color}</td>
                                <td>{hat.fabric}</td>
                                <td>{hat.style}</td>
                                <td><img src={hat.picture_url} className="img-fluid"/></td>
                                <td>{hat.location.closet_name}</td>
                                <td>
                                    <button className="btn btn-danger m-2" onClick={()=> {handleDelete(hat.id)}}>Delete</button>
                                </td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
            <NavLink className="btn btn-primary" id="new-hat-link" aria-current="page" to ="new-hat"> Create a Hat</NavLink>
            <NavLink className="btn btn-primary" id="delete-hat-link" aria-current="page" to ="delete-hat"> Delete a Hat</NavLink>
        </div>
    );
}

export default HatsList
