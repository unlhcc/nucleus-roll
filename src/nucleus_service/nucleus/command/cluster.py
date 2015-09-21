"""Usage:
      vcluster info [--user=USER]
                    [--project=PROJECT]
      vcluster list [--name=NAME]
                    [--user=USER]
                    [--project=PROJECT]
                    [--hosts=HOSTS]
                    [--start=TIME_START]
                    [--end=TIME_END]
                    [--hosts=HOSTS]
                    [--format=FORMAT]
      vcluster delete [all]
                      [--user=USER]
                      [--project=PROJECT]
                      [--name=NAME]
                      [--hosts=HOSTS]
                      [--start=TIME_START]
                      [--end=TIME_END]
                      [--host=HOST]
      vcluster delete --file=FILE
      vcluster update [--name=NAME]
                      [--hosts=HOSTS]
                      [--start=TIME_START]
                      [--end=TIME_END]
      vcluster add [--user=USER]
                   [--project=PROJECT]
                   [--hosts=HOSTS]
                   [--description=DESCRIPTION]
                   --name=NAMES
                   --start=TIME_START
                   --end=TIME_END
      vcluster add --file=FILE

    Options:
      --name=NAMEs          Names of the vcluster
      --user=USER           user name
      --project=PROJECT     project id
      --start=TIME_START    Start time of the vcluster, in
                            YYYY/MM/DD HH:MM:SS format. [default: 1901-01-01]
      --end=TIME_END        End time of the vcluster, in
                            YYYY/MM/DD HH:MM:SS format. In addition a duratio
                            can be specified if the + sign is the first sig
                            The duration will than be added to
                            the start time. [default: 2100-12-31]
      --host=HOST           host name
      --description=DESCRIPTION  description summary of the vcluster
      --file=FILE           Adding multiple vclusters from one file
      --format=FORMAT       Format is either table, json, yaml or csv
                            [default: table]
   Description:
       vcluster info
          lists the resources that support vcluster for
          a given user or project.

"""
from docopt import docopt



if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    print(arguments)
