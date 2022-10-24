from sqlalchemy import text

from api.config import get_connection

engine = get_connection()


def query_card_pegawai():
    result = engine.execute(
        text(f"""SELECT dcp.IdPegawai, jj.JenisJabatan  
			 FROM dbo.DataCurrentPegawai dcp
			 INNER JOIN dbo.Jabatan j 
			 ON dcp.KdJabatan = j.KdJabatan 
			 INNER JOIN dbo.JenisJabatan jj 
			 ON j.KdJenisJabatan = jj.KdJenisJabatan 
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    return result


def query_kategori_pegawai():
    result = engine.execute(
        text(f"""SELECT dp.IdPegawai, jp.JenisPegawai 
			 FROM dbo.DataPegawai dp
			 INNER JOIN dbo.JenisPegawai jp
			 ON dp.KdJenisPegawai = jp.KdJenisPegawai
             WHERE dp.IdPegawai <> '8888888888'
           	 ORDER BY dp.IdPegawai ASC;"""))
    return result


def query_status_pegawai():
    result = engine.execute(
        text(f"""SELECT dcp.IdPegawai, sp.Status 
			 FROM dbo.DataCurrentPegawai dcp 
			 INNER JOIN dbo.StatusPegawai sp 
			 ON dcp.KdStatus = sp.KdStatus
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    return result


def query_pendidikan_jenis_kelamin():
    result = engine.execute(
        text(f"""SELECT dcp.IdPegawai, p.Pendidikan, dp.JenisKelamin  
			FROM dbo.DataCurrentPegawai dcp 
			INNER JOIN dbo.DataPegawai dp 
			ON dcp.IdPegawai = dp.IdPegawai
			INNER JOIN dbo.KualifikasiJurusan kj  
			ON dcp.KdKualifikasiJurusan = kj.KdKualifikasiJurusan 
			INNER JOIN dbo.Pendidikan p  
			ON kj.KdPendidikan = p.KdPendidikan 
			WHERE dcp.IdPegawai <> '8888888888'
           	ORDER BY dcp.IdPegawai ASC;"""))
    return result


def query_instalasi_pegawai():
    result = engine.execute(
        text(f"""SELECT dcp.IdPegawai, i.NamaInstalasi  
			 FROM dbo.DataCurrentPegawai dcp
			 INNER JOIN dbo.Ruangan r  
			 ON dcp.KdRuanganKerja = r.KdRuangan 
			 INNER JOIN dbo.Instalasi i  
			 ON r.KdInstalasi = i.KdInstalasi  
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    return result
