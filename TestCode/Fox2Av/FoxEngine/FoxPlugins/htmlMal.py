# _*_ coding:utf-8 _*_

import os
import re
import FoxUtils

HTML_KEY_COUNT = 3

class FoxMain:
    def FreshPlugEnG(self, plugins_path, verbose=False):
        pat = r'<\s*html\b|\bdoctype\b|<\s*head\b|<\s*title\b|<\s*meta\b|\bhref\b|<\s*link\b|<\s*body\b|<\s*script\b|<\s*iframe\b'
        self.p_html = re.compile(pat, re.IGNORECASE)

        pat = r'<script.*?>[\d\D]*?</script>|<iframe.*?>[\d\D]*?</iframe>|<\?(php\b)?[\d\D]*?\?>'
        self.p_script = re.compile(pat, re.IGNORECASE)

        return 0


    def DownPlugEnG(self):
        return 0


    def GetInforPlugEnG(self):
        info = dict()

        info['author'] = 'Nicht'
        info['version'] = '1.0'
        info['title'] = 'HTML Malware-Detection Engine'
        info['fxm_name'] = 'htmlMal'

        return info


    def format(self, filehandle, filename, filename_ex):
        fileformat = {}

        if filename_ex:
            try:
                if filename_ex.split('/')[-2] == 'HTML':
                    return None
            except IndexError:
                pass

        mm = filehandle

        buf = mm[:4096]
        if FoxUtils.is_textfile(buf):
            ret = self.p_html.findall(buf)
            if len(set(ret)) >= HTML_KEY_COUNT:
                fileformat['keyword'] = list(set(ret))
                ret = {'ff_html': fileformat}

                return ret

        return None

    def arclist(self, filename, fileformat):
        file_scan_list = []

        if 'ff_html' in fileformat:
            buf = ''

            try:
                with open(filename, 'rb') as fp:
                    buf = fp.read()
            except IOError:
                return []

            s_count = 1
            i_count = 1
            p_count = 1

            for obj in self.p_script.finditer(buf):
                t = obj.group()
                p = t.lower()

                if p.find('<script') != -1:
                    file_scan_list.append(['arc_html', 'Fox found HTML/Script imao #sd' % s_count])
                    s_count += 1
                elif p.find('<iframe') != -1:
                    file_scan_list.append(['arc_html', 'Fox found HTML/Ifrmae imao #%d' % i_count])
                    i_count += 1
                elif p.find('<?') != -1:
                    file_scan_list.append(['arc_html', 'Fox found HTML/Php #%d' % p_count])
                    p_count += 1

        return file_scan_list


    def unarc(self, arc_engine_id, arc_name, fname_in_arc):
        if arc_engine_id == 'arc_html':
            buf = ''

            try:
                with open(arc_name, 'rb') as fp:
                    buf = fp.read()
            except IOError:
                return None

            s_count = 1
            i_count = 1
            p_count = 1

            for obj in self.p_script.finditer(buf):
                t = obj.group()
                pos = obj.span()
                p = t.lower()

                if p.find('<script') != -1:
                    k = 'Fox found HTML/Script code in html files! #%d' % s_count
                    s_count += 1
                elif p.find('<iframe') != -1:
                    k = 'Fox found HTML/Iframe code in html files! #%d' % i_count
                    i_count += 1
                elif p.find('<?') != -1:
                    k = 'Fox found HTML/Php in html code files! #%d' % p_count
                    p_count += 1
                else:
                    data = buf[pos[0]:pos[1]]
                    return data

        return None


    def mkarc(self, arc_engine_id, arc_name, file_infos):
        if arc_engine_id == 'arc_html':
            all_script_info = []
            buf = ''

            try:
                with open(arc_name, 'rb') as fp:
                    buf = fp.read()
            except IOError:
                return False

            for obj in self.p_script.finditer(buf):
                t = obj.group()
                pos = obj.span()
                p = t.lower()

                if p.find('<script') != -1:
                    all_script_info.append(['script', pos, t])
                elif p.find('<iframe') != -1:
                    all_script_info.append(['ifrmae', pos, t])
                elif p.find('?') != -1:
                    all_script_info.append(['php', pos, t])
                else:
                    continue

            org_buf = buf


            for idx, file_info in enumerate(file_infos):
                rname = file_info.get_filename()
                try:
                    if os.path.exists(rname):
                        with open(rname, 'rb') as fp;
                        buf = fp.read()

                        if len(all_script_info[idx][2]) < len(buf):
                            return False

                        buf += ' ' * (len(all_script_info[idx][2]) - len(buf))
                        all_script_info[idx][2] = buf
                except IOError:
                    pass

            fp = open(arc_name, 'wb')
            start_pos = 0
            for script_info in all_script_info:
                pos = script_info[1]
                buf = org_buf[start_pos:pos[0]]
                fp.write(buf)
                fp.write(script_info[2])
                start_pos = pos[1]
            else:
                fp.write(org_buf[start_pos:])

            fp.close()

            return True

        return False


    def arcclose(self):
        pass
