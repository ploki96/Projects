console.log('I am in the controller')
const Pirates = require('../models/pirate.model');

module.exports.findAllPirates = (req, res) => {
    Pirates.find({}).collation({locale: "en"}).sort({name:1})
        .then(allPirates => res.json({ results:allPirates}))
        .catch(err => res.json({ message: 'error on find all pirates', err }));
}

module.exports.findPirate = (req, res) => {
    Pirates.findOne({ _id: req.params.id})
        .then(singlePirate => res.json({results:singlePirate}))
        .catch(err => res.json({ message: 'could not find specific pirate', err}))
}

module.exports.findCaptain = (req, res) => {
    Pirates.findOne({crewPosition: "Captain"})
        .then(singlePirate => res.json({results:singlePirate}))
        .catch(err => res.json({ message: 'could not find a captain', err}))
}

module.exports.createPirate = (req, res) => {
    console.log(req.body);
    // Pirates.find({name: req.body.name}).then((user => {
    //     console.log('user ' + req.body.name )
    //     console.log('user.name ' + user )
    //     if (user.count < 1){
        Pirates.create(req.body)
            .then(pirate => res.json({ results:pirate}))
            .catch(err => res.json({ message: 'could not create pirate', err }));
        // }
        // else {
        //     console.log('else statement')
        //     res.json({err: {errors: {message: "Name must be Unique"}}})
        // }
    }
//     ))
// }

module.exports.updatePirate = (req, res) => {
    Pirates.findOneAndUpdate({_id: req.params.id},
        req.body,
        {new:true, runValidators: true})
        .then(singlePirate => res.json({results:singlePirate}))
        .catch(err => res.json({ message: 'could not update specific pirate', err}))
}

module.exports.deletePirate = (req, res) => {
    Pirates.deleteOne({_id: req.params.id})
        .then(deletedPirate => res.json({results: deletedPirate}))
        .catch(err => res.json({message: 'could not delete this pirate', err}))
}
