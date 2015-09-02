#!/usr/bin/perl -w
# nucleus roll installation test.  Usage:
# nucleus.t [nodetype]
#   where nodetype is one of "Compute", "Dbnode", "Frontend" or "Login"
#   if not specified, the test assumes either Compute or Frontend

use Test::More qw(no_plan);

my $appliance = $#ARGV >= 0 ? $ARGV[0] :
                -d '/export/rocks/install' ? 'Frontend' : 'Compute';
my $installedOnAppliancesPattern = '.';
my $isInstalled = -d '/opt/nucleus';
my $output;

my $TESTFILE = 'tmpnucleus';

if($appliance =~ /$installedOnAppliancesPattern/) {
  ok($isInstalled, 'nucleus installed');
} else {
  ok(! $isInstalled, 'nucleus not installed');
}
SKIP: {

  skip 'nucleus not installed', 4 if ! $isInstalled;
  $output = `module load nucleus; echo 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | nucleus 2>&1`;
  like($output, qr/That is correct/, 'nucleus runs');
  `/bin/ls /opt/modulefiles/applications/nucleus/[0-9]* 2>&1`;
  ok($? == 0, 'nucleus module installed');
  `/bin/ls /opt/modulefiles/applications/nucleus/.version.[0-9]* 2>&1`;
  ok($? == 0, 'nucleus version module installed');
  ok(-l '/opt/modulefiles/applications/nucleus/.version',
     'nucleus version module link created');

}

`rm -fr $TESTFILE*`;
