const mongoose = require('mongoose');

const PiratesSchema = new mongoose.Schema(
    {
        name: {
            type: String,
            required: [true, "Add a name"],
            minlength: [3, "Minimum 3 characters"]
        },
        url: {
            type: String,
            required: [true, "Add a url"],
            minlength: [3, "Minimum 3 characters"],
            maxLength: [255, "max characters is 255"]
        },
        treasureChests: {
            type: Number,
            required: [true, "Add a number of chests"],
            min: [1, "Must be positive"]
        },
        catchPhrases: {
            type: String,
            required: [true, "Add a catch phrase"],
            minlength: [3, "Minimum 3 characters"]
        },
        crewPosition: {
            type: String,
            required: [true, "Add a position"]
        },
        pegLeg: {
            type: Boolean,
            required: true
        },
        eyePatch: {
            type: Boolean,
            required: true
        },
        hookHand: {
            type: Boolean,
            required: true
        }
    }, {timestamps: true});


    const Pirates = mongoose.model("Pirates", PiratesSchema)

    module.exports = Pirates;