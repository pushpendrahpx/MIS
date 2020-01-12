import React from 'react';
import Navbar from '../Components/Navbar';
import Login from '../Components/Login';
import Register from '../Components/Register';
import { Route } from 'react-router-dom';

const Page = ()=>{
    return(<div style={{background:"teal",top:0,right:0,bottom:0,left:0,position:'absolute'}}>
        <Navbar />
        <Route path='/' exact component={Login} />
        <Route path='/register' exact component={Register} />
    </div>);
}
export default Page;