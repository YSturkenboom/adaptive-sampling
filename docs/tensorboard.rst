.. highlight:: shell

===========
Tensorboard
===========

To visualize training and validation metrics of an experiment in
Tensorboard on your local machine run

.. code-block:: bash

   tensorboard --logdir <path_to_experiment> --port <port_id>

If you are working on a remote host and want to visualize the experiment
on your local machine:

1. Run ``tensorboard --logdir <path_to_experiment> --port <remote_port_id>`` on the remote host, and
2. Run ``ssh -N -f -L localhost:<local_port_id>:localhost:<remote_port_id> <user@remote_host>`` on your local machine.
3. Navigate to ``http://localhost:<http://localhost:local_port_id>`` on your local machine.

Example
=======
+--------------------------------------------------------------+
| |direct_tensorboard|                                         |
+==============================================================+
| Tensorboard snippet of visualised validation reconstructions |
+--------------------------------------------------------------+

.. |direct_tensorboard| image:: https://user-images.githubusercontent.com/71031687/137918503-84b894e4-b9db-42cd-8e94-03bb098171fa.gif
