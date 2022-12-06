import React from 'react';

class ShoeForm extends React.Component {

    constructor(props) {
        super(props)
        this.state= {
            manufacturer: '',
            model: '',
            color: '',
            pictureUrl: '',
            bins: [],
        }

        this.handlePictureUrlChange = this.handlePictureUrlChange.bind(this);
        this.handleInputChange =this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        data.picture_url = data.pictureUrl
        data.model_name = data.model
        delete data.pictureUrl;
        delete data.model;
        delete data.bins;


        const shoeUrl = `http://localhost:8080/api/bins/${data.bin}/shoes/`;
        const fetchConfig = {
            method: 'post',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(shoeUrl, fetchConfig);
        if (response.ok) {
            const newShoe = await response.json();


            const cleared = {
                manufacturer: '',
                model: '',
                color: '',
                pictureUrl: '',
                bin: '',
            };
            this.setState(cleared);
        }
    }

    handleInputChange(event) {
        const value = event.target.value;
        this.setState({[event.target.id]: value})
    }

    handlePictureUrlChange(event) {
      const value = event.target.value;
      this.setState({pictureUrl: value})
    }

    async componentDidMount() {
        const url = 'http://localhost:8100/api/bins/';

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            this.setState({bins: data.bins})
        }
    }

    render () {
        return (
            <div className="row">
              <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                  <h1>Tell me more about your shoe!</h1>
                  <form onSubmit={this.handleSubmit} id="create-shoe-form">
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange} value={this.state.manufacturer} placeholder="Manufacturer" required type="text" name="manufacturer" id="manufacturer" className="form-control" />
                      <label htmlFor="fabric">Manufacturer</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange}value={this.state.model} placeholder="Model" required type="text" name="model" id="model" className="form-control" />
                      <label htmlFor="style">Model</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange} value={this.state.color} placeholder="Color" required type="text" name="color" id="color" className="form-control" />
                      <label htmlFor="color">Color</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handlePictureUrlChange} value={this.state.pictureUrl} placeholder="Picture URL" required type="text" name="picture_url" id="picture_url" className="form-control" />
                      <label htmlFor="picture_url">Picture URL</label>
                    </div>
                    <div className="mb-3">
                      <select onChange={this.handleInputChange} required id="bin"  name="bin" className="form-select">
                      <option value="">Choose a bin</option>
                          {this.state.bins?.map(bin => {
                              return (
                                  <option key = {bin.id} value={bin.id}>
                                      {bin.closet_name}
                                  </option>
                              )
                              })};
                      </select>
                    </div>
                    <button className="btn btn-primary">Create</button>
                  </form>
                </div>
              </div>
            </div>
        );
    }
}
export default ShoeForm;
