import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams, useHistory, Link } from "react-router-dom";
    
const Update = (props) => {
    const { id } = useParams();
    const [pirate, setPirate] = useState({});
    const [pegLeg, setPegLeg] = useState('');
    const [eyePatch, setEyePatch] = useState('');
    const [hookHand, setHookHand] = useState('');
    const history = useHistory();

    useEffect(() => {
        axios.get(`http://localhost:8000/api/pirates/${id}`)
            .then(res => {
                console.log(res)
                console.log(id)
                setPirate(res.data.results)
                setPegLeg(res.data.results.pegLeg)
                setEyePatch(res.data.results.eyePatch)
                setHookHand(res.data.results.hookHand);
            })
    }, []);
    
    const updatePirate = e => {
        e.preventDefault();
        axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
            // name,
        })
            .then(res => 
                {console.log(res)
                history.push(`/`)})
            .catch(err => console.error(err));
        
        
    }

    const updatePegLeg = e => {
        e.preventDefault();
        if (pirate.pegLeg === true){
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
            pegLeg: false
        })
            .then(res => 
                {console.log(res)
                window.location.reload(false)
                history.push(`/${id}/update`)})
            .catch(err => console.error(err));
        }
        else {
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
                pegLeg: true
            })
                .then(res => 
                    {console.log(res)
                    window.location.reload(false)
                    history.push(`/${id}/update`)})
                .catch(err => console.error(err));
        }
    }

    const updateEyePatch = e => {
        e.preventDefault();
        if (pirate.eyePatch === true){
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
            eyePatch: false
        })
            .then(res => 
                {console.log(res)
                window.location.reload(false)
                history.push(`/${id}/update`)})
            .catch(err => console.error(err));
        }
        else {
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
                eyePatch: true
            })
                .then(res => 
                    {console.log(res)
                    window.location.reload(false)
                    history.push(`/${id}/update`)})
                .catch(err => console.error(err));
        }
    }
    
    const updateHookHand = e => {
        e.preventDefault();
        if (pirate.hookHand === true){
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
            hookHand: false
        })
            .then(res => 
                {console.log(res)
                window.location.reload(false)
                history.push(`/${pirate._id}/update`)})
            .catch(err => console.error(err));
        }
        else {
            axios.patch('http://localhost:8000/api/pirates/' + id +'/update', {
                hookHand: true
            })
                .then(res => 
                    {console.log(res)
                    window.location.reload(false)
                    history.push(`/${id}/update`)})
                .catch(err => console.error(err));
        }
    }


    return (
        <div>
            <h1>{pirate.name}</h1>
            <Link to={`/`}>Home</Link>
            <div>
                <img src={pirate.url} alt={pirate.name} className='piratepic' />
                <h2>{pirate.catchPhrases}</h2>
            </div>
            <div>
                <h2>About</h2>
                <p>Position: {pirate.crewPosition}</p>
                <p>Treasures: {pirate.treasureChests}</p>
                <span>
                    <p>Peg Leg: {pirate.pegLeg === true ?
                    'Yes' 
                    : 'No'}
                    </p>
                    <button onClick={updatePegLeg}>{pirate.pegLeg === true ? 'No' : 'Yes'}</button>
                </span>
                <span>
                    <p>Eye Patch: {pirate.eyePatch === true ?
                    'Yes' 
                    : 'No'}
                    </p>
                    <button onClick={updateEyePatch}>{pirate.eyePatch === true ? 'No' : 'Yes'}</button>
                </span>
                <span>
                    <p>Hook Hand: {pirate.hookHand === true ?
                    'Yes' 
                    : 'No'}
                    </p>
                    <button onClick={updateHookHand}>{pirate.hookHand === true ? 'No' : 'Yes'}</button>
                </span>
            </div>
        </div>
    )
}
    
export default Update;