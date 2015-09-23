{
  'targets': [
    {
      'target_name': 'vio',
      'type': 'static_library',
      'standalone_static_library': 1,
      'includes': [ '../config/libmariadbclient.gypi' ],
      'sources': [
        'vio.c',
        'viosocket.c',
        'viossl.c',
        'viosslfactories.c',
      ],
      'include_dirs': [
        '.',
        '../extra/yassl/include',
        '../extra/yassl/taocrypt/include',
        '../include',
      ],
    },
  ],
}