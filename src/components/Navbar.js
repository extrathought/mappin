import React from "react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="ui two item menu">
      <NavLink to="/tweets" className="item" target="#">
        New Tweets
      </NavLink>
    </div>
  );
};

export default Navbar;
