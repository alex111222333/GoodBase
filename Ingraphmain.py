import os
import tensorflow as tf
import BetterSecurity.Utils as Utils

flags = tf.app.flags
#flags.DEFINE_integer("epoch", 25, "Epoch to train [25]")
flags.DEFINE_string("checkpoint_dir", "checkpoint", "Directory name to save the checkpoints [checkpoint]")
flags.DEFINE_string("sample_dir", "samples", "Directory name to save the samples [samples]")

flags.DEFINE_string("running_option", "Train", "Define running mode [Train,Test]")

flags.DEFINE_string("ps_hosts", "127.0.0.1:55677", "list of hostname:port pairs [hostname:port]")
flags.DEFINE_string("worker_hosts", "127.0.0.1:66788", "list of hostname:port pairs [hostname:port]")
flags.DEFINE_string("localjob_name", "PS", "Define localhost jobs [PS,WORKER]")
flags.DEFINE_integer("task_index", 0, "Index of task within the job")
flags.DEFINE_string("sync_mode", "SYNC", "Define varible update mode [SYNC,ASYN]")

FLAGS = flags.FLAGS

def main(_):
    print("----------Ingraph Main Start------------")
    # set result dirs
    print("CurrentAbsPath:", os.path.abspath(os.path.curdir))
    if not os.path.exists(FLAGS.checkpoint_dir):
        os.makedirs(FLAGS.checkpoint_dir)
    if not os.path.exists(FLAGS.sample_dir):
        os.makedirs(FLAGS.sample_dir)
    # get params
    ps_hosts = FLAGS.ps_hosts.split(",")
    worker_hosts = FLAGS.worker_hosts.split(",")
    cluster = tf.train.ClusterSpec({"PS":ps_hosts, "WORKER":worker_hosts})

    # set running opts
    # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.7)
    config = tf.ConfigProto(device_count={"CPU": 4},log_device_placement=False, allow_soft_placement=True)
    # config.gpu_options.allow_growth=True



    server = tf.train.Server(cluster, job_name=FLAGS.localjob_name, task_index=FLAGS.task_index)

    if FLAGS.localjob_name == "PS":
        server.join()
    elif FLAGS.localjob_name == "WORKER":
        print("123")
    else:
        print("----------Ingraph Err localjob_name: %s------------" % FLAGS.localjob_name)
        return

    #Net Init

    if FLAGS.running_option == 'Train':
        print("----------Ingraph Train Start------------")

    elif FLAGS.running_option == 'Test':
        print("----------Ingraph Test Start------------")

    else:
        print("----------Ingraph Err running option: %s------------" % FLAGS.running_option)
        return

    print(123)

if __name__=='__main__':
    tf.app.run()
