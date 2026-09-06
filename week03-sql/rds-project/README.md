\# AWS EC2 to Private RDS MariaDB Project



\## Project Overview



This project demonstrates how to deploy a private relational database in AWS and securely connect to it from an EC2 instance.



The goal was to combine AWS networking, Linux administration, database administration, SQL, security, and troubleshooting into one hands-on cloud engineering project.



\## Architecture



```text

&#x20;                   Internet

&#x20;                      |

&#x20;                      |

&#x20;                 SSH / HTTP

&#x20;                      |

&#x20;                      v

&#x20;            +-------------------+

&#x20;            |   Public Subnet   |

&#x20;            |                   |

&#x20;            |       EC2         |

&#x20;            | Application Server|

&#x20;            +---------+---------+

&#x20;                      |

&#x20;                      | TLS

&#x20;                      | TCP 3306

&#x20;                      |

&#x20;                      v

&#x20;            +-------------------+

&#x20;            | Private DB Tier   |

&#x20;            |                   |

&#x20;            |    Amazon RDS     |

&#x20;            |      MariaDB      |

&#x20;            +-------------------+

