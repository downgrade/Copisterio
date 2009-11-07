import os
import mimetypes
from ConfigParser import ConfigParser
from twisted.internet.task import LoopingCall

# Global configuration
__logfile__="/var/log/copisteriod.log"
__altlogfile__="/tmp/copisteriod.log"
__config_file__="foo"

class CopisterioDaemon():

    def __init__(self, cfile):
        self._conf = ConfigParser(); self._conf.read(cfile)
        self.loop = LoopingCall(self.work).start(self._c('frecuency'))
        try: self.log=open('a', __logfile__)
        except: self.log=open('a', __altlogfile__)

     def work(self):
        if self._disk_status(self._c('main')) < self._c('delete_status'):
            self._delete_files( self._get_old_files(self._c('main'), self._c('library')))

        for file in self._list_files():
            rename(self._c('tmpdir') + os.sep + file[0],
                    self._c('admdir') + os.sep + file[1] + os.sep + file[2])
            chown(getgid(), getuid(), self._c('admdir') + os.sep + files[0])
            chmod(744, self._c('admdir') + os.sep + files[0])

CopisterioDaemon(__config_file__)

class CopisterioDisk():
    # Internal functions.
    def _c(self, name): return self._conf.get('main',name)

    def _log(self,status,log):
        if self.log: self.log.write(status, '> ', log)
        else: print status, '> ', log

    def _get_disk(dir):
        # TODO Return disk where dir is.
        return

    def _disk_space(dir):
        # TODO return disk full space of _get_disk(dir)
        return

    def _disk_status(self, dir):
        # TODO Return numeric percentage of free space of _get_disk.
        return

    def _to_free(self, dir, freespace, min_free_space):
        # TODO get freespace in bytes, not percentage.
        # return min_free_space - freespace_real
        return

    def _delete_files(self, files):
        for file in files: os.unlink(file)

    def _list_files(self,dir):
        res=[]
        for root,dirs,files in os.walk(dir):
           [ rsdes.append(root + file,
             mimetypes.get_type( root + file)[0], file.__getitem__(0),
             _status(file).st_ctime, _status(file).st_size) for file in files]
        return res

    def _status(self, o): return os.stat_results(os.stat(o))

    def _get_old_files(self,maindir,dir):
        to_free = self._to_free( dir, self._disk_status(self._c('main')), 
                self._c('minspace'))
        while(to_free < freed):
            files=_list_files(self._c('main'))
            #TODO files has the data, just put in oldies the lastest ones.
            # Basically ordering an array of arrays for the third arg of each one.
            for file in oldies: freed += ofile[2]
        return oldies


