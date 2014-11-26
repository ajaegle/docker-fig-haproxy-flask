docker-fig-haproxy-flask
========================

This project contains the code used in the fig getting started and was extended to
support several backend instances load balanced by an haproxy.

Currently using hard coded host (boot2docker ip) for backends in haproxy config. 
This should be changed to use environment variables.
