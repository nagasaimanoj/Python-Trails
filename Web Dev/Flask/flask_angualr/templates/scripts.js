var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope, $http) {
    $http.get("http://localhost:5000")
        .then(function (response) {
            $scope.names = response.data;
        });
});
app.controller('urCtrl', function ($scope, $http) {
    $http.get("http://person-crud.herokuapp.com/r/getAll")
        .then(function (response) {
            $scope.names = response.data;
        });
});