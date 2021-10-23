const PiratesController = require('../controllers/pirate.controller');

module.exports = app => {
    app.get('/api/pirates', PiratesController.findAllPirates);
    app.get('/api/pirates/:id', PiratesController.findPirate);
    app.post('/api/pirates/new', PiratesController.createPirate);
    app.patch('/api/pirates/:id/update', PiratesController.updatePirate);
    app.delete('/api/pirates/:id/delete', PiratesController.deletePirate);
    app.get('/api/pirates/captain', PiratesController.findCaptain)
}