import React, { useState } from 'react'
import axios from 'axios';
import {useHistory, Link} from 'react-router-dom';

const Form = (props) => {
    const history = useHistory();

    const [name, setName] = useState(""); 
    const [url, setUrl] = useState("");
    const [treasureChests, setTreasureChests] = useState(0);
    const [catchPhrases, setCatchPhrases] = useState("");
    const [crewPosition, setCrewPosition] = useState("Captain");
    const [pegLeg, setPegLeg] = useState(true);
    const [eyePatch, setEyePatch] = useState(true);
    const [hookHand, setHookHand] = useState(true);
    const [captain, setCaptain] = useState({});


    const [errors, setErrors] = useState({});

    const onSubmitHandler = (e) => {
        e.preventDefault();
        // axios.post('http://localhost:8000/api/pirates/captain')
        //     .then(res => {
        //         if(res.data.results){
        //             setCaptain(res.data.results)
        //         }
        //     })
        
        //     console.log(`Captain Length: ${captain.captain}`)
        // if (captain && crewPosition === "Captain" ) {
        //     setErrors({err: {errors: {message: "Name must be Unique"}}})
        // }
        // else {
        axios.post('http://localhost:8000/api/pirates/new', {
            name,
            url,
            treasureChests,
            catchPhrases,
            crewPosition,
            pegLeg,
            eyePatch,
            hookHand

        })
            .then(res=>
                {console.log(res);
                
                if (res.data.results){
                    history.push('/');
                }
                else {
                    console.log(res)
                    setErrors(res.data.err.errors);
                }
                })
            .catch(err=>console.log(err))
        // }
    }

    return (
        <div>
            <h1>Favorite Pirates</h1>
            <Link to={`/`}>Crew Board</Link>
            <form onSubmit={onSubmitHandler}>
                <p>
                    <label>Pirate Name:</label><br/>
                    <input type="text" onChange={(e)=>setName(e.target.value)} />
                    {name.length < 3 && name.length >0 ? <p>First Name must be at least 3 characters long</p>: ""}
                    <span className="alert-danger">{errors.name && errors.name.message}</span>
                    
                </p>
                <p>
                    <label>Image Url</label><br/>
                    <input type="text" onChange={(e)=>setUrl(e.target.value)} />
                    {url.length < 3 && url.length >0 ? <p>URL must be at least 3 characters long</p>: ""}
                    {url.length > 255 ? <p>URL must be under 255 characters</p>: ""}
                    <span className="alert-danger">{errors.url && errors.url.message}</span>
                </p>
                <p>
                    <label># of Treasure Chests</label><br/>
                    <input type="number" onChange={(e)=>setTreasureChests(e.target.value)} />
                    {treasureChests< 0 ? <p>Treasure Chests must be a positive number</p>: ""}
                    <span className="alert-danger">{errors.treasureChests && errors.treasureChests.message}</span>
                </p>
                <p>
                    <label>Pirate Catch Phrases</label><br/>
                    <input type="text" onChange={(e)=>setCatchPhrases(e.target.value)} />
                    {catchPhrases.length < 3 && catchPhrases.length >0 ? <p>Catch Phrase must be at least 3 characters long</p>: ""}
                    <span className="alert-danger">{errors.catchPhrases && errors.catchPhrases.message}</span>
                </p>
                <p>
                    <label>crewPosition</label><br/>
                    <select onChange={(e)=>setCrewPosition(e.target.value)}>
                        <option value="Captain">Captain</option>
                        <option value="First Mate">First Mate</option>
                        <option value="Quarter Master">Quarter Master</option>
                        <option value="Boatswain">Boatswain</option>
                        <option value="Powder Monkey">Powder Monkey</option>
                    </select>
                    {/* <span className="alert-danger">{errors.name && errors.name.message}</span> */}
                </p>
                <p>
                    <label>Peg Leg</label><br/>
                    <input type="checkbox"  onClick={pegLeg==true ? (e)=>setPegLeg(false) : (e)=>setPegLeg(true)} checked={pegLeg}/>
                </p>
                <p>
                    <label>Eye Patch</label><br/>
                    <input type="checkbox"  onClick={eyePatch==true ? (e)=>setEyePatch(false) : (e)=>setEyePatch(true)} checked={eyePatch}/>
                </p>
                <p>
                    <label>Hook Hand</label><br/>
                    <input type="checkbox"  onClick={hookHand==true ? (e)=>setHookHand(false) : (e)=>setHookHand(true)} checked={hookHand}/>
                </p>
                <input type="submit"/>
            </form>
        </div>
    )
}

export default Form;