import { NavLink } from "react-router-dom";

function HatsList(props) {
    return (
        <div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Color</th>
                        <th>Fabric</th>
                        <th>Style</th>
                        <th>Location</th>
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
                                <td>{hat.location}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
            <NavLink className="btn brn-primary" id="new-hat-link" aria-current="page" to ="new"> Create a Hat</NavLink>
        </div>
    );
}

export default HatsList
