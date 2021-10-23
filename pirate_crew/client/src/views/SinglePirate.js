import React, { useEffect, useState } from 'react'
import axios from 'axios';
import {useParams, Link} from 'react-router-dom';

const SinglePirate = (props) => {
    const [singlePirate, SetSinglePirate] = useState({});
    const {id} = useParams();

    
    useEffect(()=>{
        axios.get(`http://localhost:8000/api/pirates/${id}`)
            .then(res=> SetSinglePirate(res.data.results))  
            .catch(err =>console.log(err))
    }, [id]);

    return(
        <div>
            <p>{singlePirate.name}</p>
            <Link to={`/${id}/update`}>Edit</Link>
        </div>
    )
}
export default SinglePirate;