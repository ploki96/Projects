const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator')

const UsersSchema = new mongoose.Schema(
    {
        first_name: {
            type: String,
            required: [true, "Add a first name"],
            minlength: [3, "Minimum 3 characters"],
        },
        last_name: {
            type: String,
            required: [true, "Add a name"],
            minlength: [3, "Minimum 3 characters"],
        },
        email: {
            type: String,
            required: [true, "Add a name"],
            minlength: [5, "Minimum 3 characters"],
            unique: [true,"User must be unique"]
        },
        password: {
            type: String,
            required: [true, "Add a name"],
            minlength: [8, "Minimum 3 characters"],
        }

    }, {timestamps: true});

    UsersSchema.plugin(uniqueValidator)

    const Users = mongoose.model("Users", UsersSchema)

    module.exports = Users;