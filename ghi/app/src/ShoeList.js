function ShoesList(props) {
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
            {props.shoes?.map(shoe => {
              return (
                <tr key={shoe.href}>
                  <td>{ shoe.manufacturer }</td>
                  <td>{ shoe.color }</td>
                  <td>{ shoe.model_name }</td>
                </tr>
              );
            })}
            </tbody>
          </table>
      );
}



export default ShoesList;
