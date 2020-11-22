import React from "react";
import { Component } from 'react';
/* import { TwitterTweetEmbed } from "react-twitter-embed";
*/
import GoogleMapReact from 'google-map-react';

const Tweet = ({ json }) => {
  const { id } = json.data;

   const options = {
    cards: "hidden",
    align: "center",
    width: "550",
    conversation: "none",
  };
   console.log(json.data);

 /*  return <TwitterTweetEmbed options={options} tweetId={id} />;*/
};


const AnyReactComponent = ({ text }) => <div>{text}</div>;
 
class SimpleMap extends Component {
  static defaultProps = {
    center: {
      lat: 59.95,
      lng: 30.33
    },
    zoom: 11
  };
 
  render() {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyAxtCkpjNugeo6LDZ7VdTTbu2ti575WYU4'}}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <AnyReactComponent
            lat={59.955413}
            lng={30.337844}
            text="My Marker"
          />
        </GoogleMapReact>
      </div>
    );
  }
}
export default SimpleMap;


