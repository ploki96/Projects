const UsersController = require('../controllers/user.controller');

module.exports = app => {
    app.get('/api/users', UsersController.findAllUsers);
    app.get('/api/users/:id', UsersController.findUser);
    app.post('/api/users/new', UsersController.createUser);
    app.patch('/api/users/:id/update', UsersController.updateUser);
    app.delete('/api/users/:id/delete', UsersController.deleteUser)
}