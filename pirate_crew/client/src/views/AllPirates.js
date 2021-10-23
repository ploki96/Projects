import React, { useState, useEffect } from 'react'
import axios from 'axios';
import {useHistory, useParams, Link} from 'react-router-dom';

const AllPirates = (props) => {
    const [pirates, setPirates] = useState([]);
    const history = useHistory();
    const { removeFromDom } = props;

    useEffect(() => {
        axios.get("http://localhost:8000/api/pirates")
            .then(res => setPirates(res.data.results))
    }, [pirates])

    // const onClickHandler = (e) => {
    //     e.preventDefault();
    //     history.push(`/pirates/${e.target.id}`)
    // }
    
    const deletePirate = (_id) => {
        axios.delete(`http://localhost:8000/api/pirates/${_id}/delete`)
            .then(res => {
                removeFromDom(_id)
                history.push('/')
            })
            .catch(err => console.error(err));
    }

    const editPirate = (_id) => {
        history.push(`/${_id}/update`)
    }

    return (
        <div>
            <h1>Pirate Crew</h1>
            <Link to={`/add`}>Add an Pirate</Link>
            {
                pirates.map ((pirate, i) => {
                    return (
                        <div>
                            <p>{pirate.name}</p>
                            <img class='piratepic' src={pirate.url} alt={pirate.name}/>
                            <button onClick={(e) =>editPirate(pirate._id)}>View Pirate</button>
                            <button onClick={(e) =>deletePirate(pirate._id)}>Walk the Plank</button>
                        </div>
                        
                    )
                })
            }

        </div>
    )
}

export default AllPirates;