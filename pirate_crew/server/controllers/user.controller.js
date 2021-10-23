const Users = require('../models/user.model');

module.exports.findAllUsers = (req, res) => {
    Users.find({}).sort({name:1})
        .then(allUsers => res.json({ results:allUsers}))
        .catch(err => res.json({ message: 'error on find all users', err }));
}

module.exports.findUser = (req, res) => {
    Users.findOne({ _id: req.params.id})
        .then(singleUser => res.json({results:singleUser}))
        .catch(err => res.json({ message: 'could not find specific user', err}))
}

module.exports.createUser = (req, res) => {
    console.log(req.body);
    // Users.find({name: req.body.name}).then((user => {
    //     console.log('user ' + req.body.name )
    //     console.log('user.name ' + user )
    //     if (user.count < 1){
        Users.create(req.body)
            .then(user => res.json({ results:user}))
            .catch(err => res.json({ message: 'could not create user', err }));
        // }
        // else {
        //     console.log('else statement')
        //     res.json({err: {errors: {message: "Name must be Unique"}}})
        // }
    }
//     ))
// }

module.exports.updateUser = (req, res) => {
    Users.findOneAndUpdate({_id: req.params.id},
        req.body,
        {new:true, runValidators: true})
        .then(singleUser => res.json({results:singleUser}))
        .catch(err => res.json({ message: 'could not update specific user', err}))
}

module.exports.deleteUser = (req, res) => {
    Users.deleteOne({_id: req.params.id})
        .then(deletedUser => res.json({results: deletedUser}))
        .catch(err => res.json({message: 'could not delete this user', err}))
}
