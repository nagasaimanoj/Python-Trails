let app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope, $http) {
    $http.get("http://127.0.0.1:5000/data")
        .then(function (response) {
            $scope.names = response.data;
        });
});