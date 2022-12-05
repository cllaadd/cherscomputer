import React from 'react';

class HatForm extends React.Component {

    constructor(props) {
        super(props)
        this.state= {
            fabric: '',
            style: '',
            color: '',
            pictureUrl: '',
            locations: [],
        }
        this.handlePictureUrlChange = this.handlePictureUrlChange.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        data.picture_url = data.pictureUrl
        delete data.pictureUrl;
        delete data.locations;

        const hatUrl = `http://localhost:8090/api/locations/${data.location}/hats/`;
        const fetchConfig = {
            method: 'post',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(hatUrl, fetchConfig);
        if (response.ok) {
            const newHat = await response.json();

            const cleared = {
                fabric: '',
                style: '',
                color: '',
                pictureUrl: '',
                location: '',
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
        const url = 'http://localhost:8100/api/locations/';

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            this.setState({locations: data.locations})
        }
    }

    render () {
        return (
            <div className="row">
              <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                  <h1>Tell me more about your hat!</h1>
                  <form onSubmit={this.handleSubmit} id="create-hat-form">
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange} value={this.state.fabric} placeholder="Fabric" required type="text" name="fabric" id="fabric" className="form-control" />
                      <label htmlFor="fabric">Fabric</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange} value={this.state.style} placeholder="Style" required type="text" name="style" id="style" className="form-control" />
                      <label htmlFor="style">Style</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handleInputChange} value={this.state.color} placeholder="Color" required type="text" name="color" id="color" className="form-control" />
                      <label htmlFor="color">Color</label>
                    </div>
                    <div className="form-floating mb-3">
                      <input onChange={this.handlePictureUrlChange} value={this.state.pictureUrl} placeholder="Picture URL" required type="url" name="picture_url" id="picture_url" className="form-control" />
                      <label htmlFor="picture_url">Picture URL</label>
                    </div>
                    <div className="mb-3">
                      <select onChange={this.handleInputChange} required id="location"  name="location" className="form-select">
                      <option value="">Choose a location</option>
                          {this.state.locations?.map(location => {
                              return (
                                  <option key = {location.id} value={location.id}>
                                      {location.closet_name}
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
export default HatForm
